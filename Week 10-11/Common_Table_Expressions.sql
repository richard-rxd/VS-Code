CREATE TABLE TrainingDB.tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(100),
    category VARCHAR(100),
    priority INT,
    completed BOOLEAN,
    deadline DATE
);

INSERT INTO TrainingDB.tasks (task_name, category, priority, completed, ≈)
VALUES
    ('Task 1', 'Work', 1, true, '2024-05-10'),
    ('Task 2', 'Personal', 2, false, '2024-05-15'),
    ('Task 3', 'Work', 3, false, '2024-05-12'),
    ('Task 4', 'Personal', 1, true, '2024-05-20'),
    ('Task 5', 'Work', 2, true, '2024-05-18'),
    ('Task 6', 'Work', 2, false, '2024-05-22');

-- @block
-- Calculate the total number of tasks in each category.
SELECT
    tasks.category,
    COUNT(tasks.task_name)
FROM
    TrainingDB.tasks
GROUP BY
    tasks.category;

-- @block
-- Find the average priority of completed tasks and incomplete tasks.
SELECT
    DISTINCT CASE WHEN tasks.completed THEN "Completed" ELSE "Not Completed" END,
    AVG(tasks.priority) OVER(PARTITION BY CASE WHEN tasks.completed THEN "Completed" ELSE "Not Completed" END) as AVG_Priority
FROM
    TrainingDB.tasks;

-- @block
-- Calculate the percentage of completed tasks for each category.
SELECT
    tasks.category,
    CONCAT(CAST(SUM(tasks.completed) / COUNT(tasks.id) * 100 AS DECIMAL(5,2)) , "%")
FROM
    TrainingDB.tasks
GROUP BY
    tasks.category;
-- @block
-- Find the task with the earliest deadline in each category.
SELECT
    tasks.category,
    MIN(tasks.deadline)
FROM
    TrainingDB.tasks
GROUP BY
    tasks.category;

-- @block
-- Calculate the running total of completed tasks over the deadline for each category.
SELECT
    tasks.category,
    tasks.deadline,
    SUM(tasks.completed) OVER(PARTITION BY category ORDER BY tasks.deadline) AS Completed
FROM
    TrainingDB.tasks

-- @block
-- Use a CTE to find the tasks that are due within the next 7 days.
WITH due_next AS (
    SELECT
        tasks.task_name
    FROM
        TrainingDB.tasks
    WHERE
        DATEDIFF(DATE_ADD(CURDATE(), INTERVAL 7 DAY), tasks.deadline) < 8 AND DATEDIFF(DATE_ADD(CURDATE(), INTERVAL 7 DAY), tasks.deadline) > 0
)
SELECT *
FROM due_next;
