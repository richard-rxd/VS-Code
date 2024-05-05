
-- @block
CREATE TABLE pillars(
    id INT AUTO_INCREMENT,
    pillar varchar(255) NOT NULL unique,
    goals text,
    primary key (id)
)
-- @block
create table workspaces(
    id int AUTO_INCREMENT,
    workspace varchar(255) not null unique,
    status enum("Active", "Planned", "Completed", "Canceled"),
    pillar_id int,
    workspace_goal text,
    primary key (id),
    foreign key (pillar_id) references pillars(id)
)
-- @block
create table projects(
    id int AUTO_INCREMENT,
    project varchar(255) not null unique,
    priority enum("ASAP", "High", "Medium", "Low"),
    status enum("In Progress", "Todo", "Planned", "Monitoring", "Completed", "Canceled"),
    deadline date,
    dependencies_id int,
    workspace_id int,
    schedule_now boolean,
    schedule_next boolean,
    primary key (id),
    foreign key (dependencies_id) references projects(id),
    foreign key (workspace_id) references workspaces(id)
)
-- @block
create table tasks(
    id int AUTO_INCREMENT,
    task varchar(255) not null,
    priority enum("ASAP", "High", "Medium", "Low"),
    status enum("Completed", "In Progress", "Todo", "Planned", "Canceled"),
    deadline date,
    notes text,
    schedule_now boolean,
    schedule_next boolean,
    project_id int,
    primary key (id),
    foreign key (project_id) references projects(id)
)
-- @block
create table recurring_tasks(
    id int auto_increment,
    task varchar(255) not null unique,
    status enum("Active", "On Hold") default "On Hold",
    timeframe enum("Daily", "Weekly", "Monthly"),
    time_cost time,
    workspace_id int,
    primary key (id),
    foreign key (workspace_id) references workspaces(id)
)



-- @block
-- Default Values zu Status in Priority in jeder Tabelle hinzugefügt
-- Warum musste ich jedes statement mit einem Block trennen?
alter table workspaces alter status set default "Planned";
alter table projects alter status set default "Planned";
alter table projects alter priority set default "Low";
alter table tasks alter status set default "Planned";
alter table tasks alter priority set default "Low";
alter table projects alter schedule_now set default 0; 
alter table projects alter schedule_next set default 0;
alter table tasks alter schedule_next set default 0; 
alter table tasks alter schedule_next set default 0;  

-- @block
-- Trigger hinzugefügt um zu tracken wann eine Task scheduled wurde
alter table tasks add scheduled_time date;
create trigger track_scheduled_time before update on tasks 
for each row 
begin 
    if old.schedule_now != new.schedule_now or old.schedule_next != new.schedule_next then 
        set new.scheduled_time = current_date();
    end if;
end;
-- @block
-- Trigger hinzugefügt um zu tracken wann eine Project scheduled wurde
alter table projects add scheduled_time date;
create trigger track_scheduled_time_project before update on projects 
for each row 
begin 
    if old.schedule_now != new.schedule_now or old.schedule_next != new.schedule_next then 
        set new.scheduled_time = current_date();
    end if;
end;



-- @block
-- Testdaten in Tabellen eintragen
insert into pillars (pillar, goals) 
values 
    ("Family & Friends", "Mehr Zeit mit F&F verbringen"),
    ("Competent & Skilled", "Python AI Grundlagen beherrschen - LLM Tools selber bauen"),
    ("Financial Freedom", "Eine zuverlässige Einkommensquelle aufbauen"),
    ("Healthy Body & Mind", "Körpergewicht < 99kg");
insert into workspaces (workspace, pillar_id, status, workspace_goal)
values
    ("AI Engineering / Coding Basic", 2, "Active", "Skills im Software & Programmieren Bereich ausbauen; Python lernen; Basic für AI und LLM Engineering lernen"),
    ("OM", 3, "Active", "Cashflow für Lebensunterhalt"),
    ("Investing", 3, "Active", "Vermögen vor Inflation & Entwertung schützen und ggf. vermehren"),
    ("Gym", 4, "Active", ""),
    ("Greece", 1, "Planned", "");
insert into projects (project, priority, status, deadline, dependencies_id, workspace_id)
values
    -- Default Value wird bei "null" nicht eingetragen - MEGA CRINGE
    ("AI Engineering Kurs", "High", "In Progress", "2024-06-15", NULL, 1);
    ("IR Account Management", "Medium", "In Progress", null, null, 3),
    ("OM Prozesse optimieren + automatisieren", "Medium", null, null, null, 2),
    ("IG Content Schedule erstellen", "Medium", null, null, 3, 2),
    ("AirBnB suchen & buchen", null, null, "2024-06-01", null, 5);
insert into recurring_tasks (task, recurring_tasks.status, timeframe, time_cost, workspace_id)
values
    ("Gym", "Active", "Daily", '01:30:00', 4),
    ("Lesen", "Active", "Daily", '01:00:00', null),
    ("Wochen Schedule erstellen", "Active", "Daily", '01:30:00', null),
    ("Family Skypen", "Active", "Weekly", '01:00:00', null),
    ("Staubsaugen", "Active", "Weekly", '01:00:00', null),
    ("Qnology Report lesen", "Active", "Daily", '01:00:00', 3),
    ("FH Börsenbrief lesen", "Active", "Monthly", '02:00:00', 3);
-- @block
insert into tasks (task, status, priority, notes, project_id)
values
    ("SQL Kapitel abschließen", "In Progress", "High", "", 1),
    ("Math & Statistic Kapitel abschließen", "Todo", "High", "", 1),
    ("Cash Holdings effizienter gestalten", "Todo", "Medium", "", 2),
    ("Content Datenbank erstellen", "Todo", "Medium", "", 3),
    ("Informieren über mögliche US LNG Invests", "Completed", "Medium", "", 2),
    ("Informieren über optimalere Aufwärmung", "Planned", "Low", "", null);

-- @block
-- Tasks Tabelle Anschicht
create view tasks_view as
    select 
        tasks.task, 
        tasks.status, 
        tasks.priority, 
        tasks.deadline, 
        case
            when projects.dependencies_id is null then "No Dependencies"
            else "Unsolved Dependencies"
        end as "Dependencies",
        case
            -- when WEEKOFYEAR(tasks.scheduled_time) >= WEEKOFYEAR(current_date() then "This Week")
            when weekofyear(tasks.scheduled_time) >= WEEKOFYEAR(CURDATE()) and tasks.schedule_now = 1 then "This Week"
            when weekofyear(tasks.scheduled_time) >= WEEKOFYEAR(CURDATE()) and tasks.schedule_next = 1 then "Next Week"
            when weekofyear(tasks.scheduled_time) >= WEEKOFYEAR(CURDATE()) - 1 and tasks.schedule_next = 1 then "This Week"
            else "Not Scheduled"
        end as "Schedule",
        projects.project, 
        workspaces.workspace,
        pillars.pillar
    from tasks
    left join 
        projects on project_id = projects.id
    left join    
        workspaces on projects.workspace_id = workspaces.id
    right join
        pillars on workspaces.pillar_id = pillars.id
    order by 
        workspaces.pillar_id is null, 
        case 
            WHEN WEEKOFYEAR(tasks.scheduled_time) >= WEEKOFYEAR(CURDATE()) AND tasks.schedule_now = 1 THEN 1
            WHEN WEEKOFYEAR(tasks.scheduled_time) >= WEEKOFYEAR(CURDATE()) AND tasks.schedule_next = 1 THEN 2
            WHEN WEEKOFYEAR(tasks.scheduled_time) >= WEEKOFYEAR(CURDATE()) - 1 AND tasks.schedule_next = 1 THEN 1
            else 3
        end, 
        pillars.pillar;

-- @block
-- Recurring Tasks Tabelle Anschicht
create view recurring_tasks_view as
    select
        recurring_tasks.task,
        concat(cast(round(time_to_sec(recurring_tasks.time_cost) / 60) as unsigned), "min") as Duration,
        recurring_tasks.timeframe,
        workspaces.workspace,
        pillars.pillar
    from recurring_tasks
    left join
        workspaces on recurring_tasks.workspace_id = workspaces.id
    left join
        pillars on workspaces.pillar_id = pillars.id
    order by
        case
            when recurring_tasks.timeframe = "Daily" then 1
            when recurring_tasks.timeframe = "Weekly" then 2
            when recurring_tasks.timeframe = "Monthly" then 3
        end,
        Duration ASC,
        workspace_id is null;
-- @block
-- Workspace Tabelle Anschicht
-- create view workspaces_view as
    select
        w.workspace as Workspace,
        w.status as Status,
        group_concat(distinct projects.project separator ", ") as Projects,
        count(distinct projects.project) as Total_Projects,
        concat(cast((sum(case when projects.status = "Completed" then 1 else 0 end) / count(distinct projects.project)) * 100 as decimal(5,2)), "%") as Completed,
        group_concat(distinct recurring_tasks.task separator ", ") as Recurring_Tasks,
        -- Schrott: concat(cast(ifnull(sum(recurring_tasks.time_cost), 0) / 60 as unsigned), "min") as Time_Cost,
        -- Schrott: sec_to_time(ifnull(sum(recurring_tasks.time_cost), 0)) as Time_Cost2,
        w.workspace_goal as Goal,
        pillars.pillar as Pillar,
    from workspaces w
    right join
        pillars on pillars.id = w.pillar_id
    left join
        projects on w.id = projects.workspace_id
    left join
        recurring_tasks on recurring_tasks.workspace_id = w.id
    group by
        w.workspace, w.status, w.workspace_goal, pillars.pillar;
-- @block
-- Does not work
SELECT 
    w.workspace,
    COALESCE(SUM(rt.total_time_cost), 0) AS Time_Cost
FROM 
    workspaces w
LEFT JOIN 
    (
        SELECT 
            workspace_id,
            SUM(time_cost) AS total_time_cost
        FROM 
            recurring_tasks
        GROUP BY 
            workspace_id
    ) rt ON w.id = rt.workspace_id
GROUP BY 
    w.id;

-- @block
-- SCHROTT - Versuch 2: Zeitaufwand der Recurring Tasks pro Tag zu kalkulieren
select 
    workspace_id, 
    sec_to_time(
        cast(
            round(
                    sum(case
                        when recurring_tasks.timeframe = "Daily" then recurring_tasks.time_cost
                        when recurring_tasks.timeframe = "Weekly" then (recurring_tasks.time_cost / 7)
                        when recurring_tasks.timeframe = "Monthly" then (recurring_tasks.time_cost / 30)
                    end) / 60
            ) * 60
        as unsigned
        )
    ) as Time_Cost
from 
    recurring_tasks 
group by 
    workspace_id

-- @block
-- SCHROTT
select 
    workspace_id, 

                    sum(case
                        when recurring_tasks.timeframe = "Daily" then recurring_tasks.time_cost * 30
                        when recurring_tasks.timeframe = "Weekly" then (recurring_tasks.time_cost * 4.2)
                        when recurring_tasks.timeframe = "Monthly" then (recurring_tasks.time_cost)
                    end)
from 
    recurring_tasks 
group by 
    workspace_id, recurring_tasks.timeframe, recurring_tasks.time_cost;



-- @block
-- procdures verstehn + weitere tools verstehen / vertraut machen, erste Views erstellen von tabelle (siehe chatgpt)