-- -----------------------------------------------------
-- changes on property
-- -----------------------------------------------------

ALTER TABLE property ADD COLUMN status_id INT NOT NULL;

ALTER TABLE property  ADD CONSTRAINT fk_property_status FOREIGN KEY
(status_id) REFERENCES status(id);

-- -----------------------------------------------------
-- user_like_property`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS user_like_property (
  id INT NOT NULL,
  property_id INT NOT NULL,
  user_id INT NOT NULL,
  like_date DATETIME NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_user_like_property
    FOREIGN KEY (user_id)
    REFERENCES auth_user(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_user_like_property_property
    FOREIGN KEY (property_id)
    REFERENCES property (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

