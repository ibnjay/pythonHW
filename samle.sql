select 
    item.country_name
    , item.motor_cycle_model
    , sum(COALESCE(sales.quantity * item.price,0)) as revenue
from    
   (select con.id as cid
      , con.name as country_name
      , mm.id as mid
      , mm.name as motor_cycle_model
      , mm.price as price
    from country con
    cross join motorcycle_model mm
   ) item
left join sales on sales.model_id=item.mid
                  and sales.country_id=item.cid
                  and year(sales.sales_date) = 2018
group by 1,2
order by 1;


WITH item AS (select con.id as country_id
      , con.name as country_name
      , mm.id as model_id
      , mm.name as motor_cycle_model
      , mm.price as price
    from country con
    cross join motorcycle_model mm) 
  
SELECT item.country_name, item.motor_cycle_model, sum(COALESCE(sales.quantity * item.price,0)) as revenue

from item left join sales on sales.model_id = item.model_id
                            and sales.country_id = item.country_id
                            and year(sales.sales_date) = 2018
group by 1,2 ;  



select employee.name,
    CASE
    WHEN eu.uin is NULL THEN 'NULL'
    WHEN eu.uin = '' THEN 'NULL'
    ELSE eu.uin 
    END AS uin
from employee left join employee_uin eu on employee.id = eu.id

