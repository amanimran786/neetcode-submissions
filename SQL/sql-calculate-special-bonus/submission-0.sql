-- Write your query below
Select e.employee_id,
    Case
        When e.employee_id %2 = 1
            And e.name Not Like 'M%'
        Then e.salary
        Else 0
    End As bonus
From employees As e
Order by e.employee_id;
