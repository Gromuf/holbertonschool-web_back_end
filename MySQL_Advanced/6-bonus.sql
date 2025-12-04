-- 6-bonus.sql
DELIMITER $$

CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN bonus_score INT
)
BEGIN
	DECLARE proj_id INT;

	SELECT id INTO proj_id
	FROM project
	WHERE name = project_name;
	LIMIT 1;

	IF proj_id IS NULL THEN
		INSERT INTO project (name)
		VALUES (project_name);
		SET proj_id = LAST_INSERT_ID();
	END IF;

	INSERT INTO bonus (user_id, project_id, score)
	VALUES (user_id, proj_id, bonus_score);
END$$

DELIMITER ;
