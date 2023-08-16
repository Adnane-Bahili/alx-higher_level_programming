-- Lists all the Californian cities in the "hbtn_0d_usa" database 
-- Results ordered by ascending cities.id
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
