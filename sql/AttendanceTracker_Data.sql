Use AttendanceTracker;
INSERT INTO students VALUES
(1, 'Quinn', 'Fricko'),
(2, 'Olivia', 'Walton'),
(3, ' Jade ', 'ODowd');

INSERT INTO courses VALUES
(1001, '10:00-11:00', 'Biology'),
(1002, '11:00-12:00', 'Database Management');


INSERT INTO attendance VALUES
(1001, 1, '2025-07-13', 'Present'),
(1001, 2, '2025-07-13', 'Absent'),
(1001, 3, '2025-07-13', 'Present'),
(1002, 1, '2025-07-13', 'Present'),
(1002, 2, '2025-07-13', 'Present'),
(1002, 3, '2025-07-13', 'Absent'),
(1001, 1, '2025-07-14', 'Present'),
(1001, 2, '2025-07-14', 'Present'),
(1001, 3, '2025-07-14', 'Absent');
