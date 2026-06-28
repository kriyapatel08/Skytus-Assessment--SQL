CREATE DATABASE MessManagementSystem;

USE MessManagementSystem;

--Student Table (Stores Student Information System)

CREATE TABLE Students
(
    StudentID INT PRIMARY KEY IDENTITY(1,1),
    FullName VARCHAR(100),
    Gender VARCHAR(10),
    Department VARCHAR(50),
    Phone VARCHAR(15),
    RoomNo VARCHAR(10),
    JoinDate DATE
);

--Staff Table(Storesb mess workers.)

CREATE TABLE Staff
(
    StaffID INT PRIMARY KEY IDENTITY(1,1),
    StaffName VARCHAR(100),
    Role VARCHAR(50),
    Phone VARCHAR(15),
    Salary DECIMAL(10,2)
);

--3. MealPlans Table(Monthely mess plans)

CREATE TABLE MealPlans
(
    PlanID INT PRIMARY KEY IDENTITY(1,1),
    PlanName VARCHAR(50),
    MonthlyFee DECIMAL(10,2)
);

--4. StudentMealPlan Table(Which student has which meal plan.)

CREATE TABLE StudentMealPlan
(
    StudentID INT,
    PlanID INT,
    StartDate DATE,

    PRIMARY KEY(StudentID, PlanID),

    FOREIGN KEY(StudentID)
        REFERENCES Students(StudentID),

    FOREIGN KEY(PlanID)
        REFERENCES MealPlans(PlanID)
);

--5. DailyMenu Table(Stores menu of every day.)

CREATE TABLE DailyMenu
(
    MenuID INT PRIMARY KEY IDENTITY(1,1),
    MenuDate DATE,
    Breakfast VARCHAR(100),
    Lunch VARCHAR(100),
    Dinner VARCHAR(100)
);

--6. Attendance Table(Stores meal attendance.)

CREATE TABLE Attendances
(
    AttendanceID INT PRIMARY KEY IDENTITY(1,1),
    StudentID INT,
    MenuID INT,
    MealType VARCHAR(20),
    Status VARCHAR(20),

    FOREIGN KEY(StudentID)
        REFERENCES Students(StudentID),

    FOREIGN KEY(MenuID)
        REFERENCES DailyMenu(MenuID)
);

--7. Payments Table(Stores payment history.)

CREATE TABLE Payments
(
    PaymentID INT PRIMARY KEY IDENTITY(1,1),
    StudentID INT,
    Amount DECIMAL(10,2),
    PaymentDate DATE,
    PaymentMode VARCHAR(20),
    Status VARCHAR(20),

    FOREIGN KEY(StudentID)
        REFERENCES Students(StudentID)
);

--Insert Sample Data

--Students
INSERT INTO Students
VALUES
('Rahul Patel','Male','Computer','9876543210','A101','2025-01-10'),
('Priya Shah','Female','Mechanical','9876543211','B201','2025-01-11'),
('Amit Kumar','Male','Civil','9876543212','C301','2025-01-12'),
('Neha Patel','Female','IT','9876543213','A202','2025-01-15'),
('Rohan Mehta','Male','Computer','9876543214','B101','2025-01-18');

--staff

INSERT INTO Staff
VALUES
('Mahesh','Cook','9876500011',25000),
('Rakesh','Cook','9876500012',22000),
('Suresh','Cleaner','9876500013',15000),
('Asha','Helper','9876500014',18000);

--Meal Plans

INSERT INTO MealPlans
VALUES
('Regular',2500),
('Premium',3500);

--Student Meal Plan

INSERT INTO StudentMealPlan
VALUES
(1,1,'2025-01-01'),
(2,2,'2025-01-01'),
(3,1,'2025-01-01'),
(4,2,'2025-01-01'),
(5,1,'2025-01-01');

--Daily Menu

INSERT INTO DailyMenu
VALUES
('2025-06-01','Poha','Dal Rice','Chapati Sabji'),
('2025-06-02','Upma','Paneer Rice','Khichdi'),
('2025-06-03','Idli','Veg Biryani','Dal Fry');

--Attendance

INSERT INTO Attendances
VALUES
(1,1,'Breakfast','Present'),
(2,1,'Lunch','Present'),
(3,2,'Dinner','Absent'),
(4,3,'Lunch','Present'),
(5,2,'Breakfast','Present');

--Payments

INSERT INTO Payments
VALUES
(1,2500,'2025-06-01','UPI','Paid'),
(2,3500,'2025-06-01','Cash','Paid'),
(3,2500,'2025-06-02','Card','Paid'),
(4,3500,'2025-06-02','UPI','Pending'),
(5,2500,'2025-06-03','Cash','Paid');

SELECT * FROM Students;

SELECT *
FROM Students
WHERE Department='Computer';

--Students with Premium plan.

SELECT s.FullName,p.PlanName

FROM Students s

JOIN StudentMealPlan sm
ON s.StudentID=sm.StudentID

JOIN MealPlans p
ON sm.PlanID=p.PlanID

WHERE p.PlanName='Premium';

--Total students.

SELECT COUNT(*) AS TotalStudents
FROM Students;

--Total monthly payment collected.

SELECT SUM(Amount) AS TotalCollection
FROM Payments
WHERE Status='Paid';

--Pending payments.

SELECT *
FROM Payments
WHERE Status='Pending';

--Students absent for meals.

SELECT s.FullName,a.MealType

FROM Students s

JOIN Attendance a
ON s.StudentID=a.StudentID

WHERE a.Status='Absent';

--Today's menu.

SELECT *
FROM DailyMenu;

--Highest salary staff.

SELECT TOP 1 *
FROM Staff
ORDER BY Salary DESC;

--Average staff salary.

SELECT AVG(Salary)
FROM Staff;

--Students who paid using UPI.

SELECT s.FullName,p.PaymentMode

FROM Students s

JOIN Payments p

ON s.StudentID=p.StudentID

WHERE PaymentMode='UPI';

--Number of students in each department.

SELECT Department,
COUNT(*) AS Total

FROM Students

GROUP BY Department;

--Total attendance records.

SELECT COUNT(*)
FROM Attendances;

--Breakfast menu.

SELECT MenuDate,Breakfast
FROM DailyMenu;

--Student payment report.

SELECT
s.FullName,
p.Amount,
p.Status

FROM Students s

JOIN Payments p

ON s.StudentID=p.StudentID;

--Index 1: Search Students by Department

CREATE INDEX IX_Students_Department
ON Students(Department);

SELECT *
FROM Students
WHERE Department='Computer';

--Index 2: Search Payments by Student

CREATE INDEX IX_Payments_StudentID
ON Payments(StudentID);

SELECT *
FROM Payments
WHERE StudentID=3;

--Index 3: Search Attendance by Student

CREATE INDEX IX_Attendance_StudentID
ON Attendances(StudentID);

SELECT *
FROM Attendances
WHERE StudentID=2;