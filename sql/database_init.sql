-- DROP SCHEMA taco;
CREATE SCHEMA taco AUTHORIZATION taco;


-- DROP TABLE taco.dishes;
CREATE TABLE taco.dishes (
	"uuid" uuid NOT NULL,
	"name" varchar NOT NULL,
	CONSTRAINT dishes_pk PRIMARY KEY (uuid)
);


-- DROP TABLE taco.ingredients;
CREATE TABLE taco.ingredients (
	"uuid" uuid NOT NULL,
	"name" varchar NOT NULL,
	CONSTRAINT ingredients_pk PRIMARY KEY (uuid)
);


-- DROP TABLE taco.measurement_units;
CREATE TABLE taco.measurement_units (
	"uuid" uuid NOT NULL,
	"name" varchar NOT NULL,
	abbreviation varchar NOT NULL,
	CONSTRAINT measurement_units_pk PRIMARY KEY (uuid)
);


-- DROP TABLE taco.nutritional_values;
CREATE TABLE taco.nutritional_values (
	"uuid" uuid NOT NULL,
	ingredient_uuid uuid NOT NULL,
	measurement_unit_uuid uuid NOT NULL,
	calories numeric NOT NULL,
	fats numeric NOT NULL,
	carbohydrates numeric NOT NULL,
	proteins numeric NOT NULL,
	sodium numeric NOT NULL,
	fiber numeric NOT NULL,
	CONSTRAINT nutritional_values_pk PRIMARY KEY (uuid),
	CONSTRAINT nutritional_values_ingredients_fk FOREIGN KEY (ingredient_uuid) REFERENCES taco.ingredients("uuid") ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT nutritional_values_measurement_units_fk FOREIGN KEY (measurement_unit_uuid) REFERENCES taco.measurement_units("uuid") ON DELETE RESTRICT ON UPDATE RESTRICT
);


-- DROP TABLE taco.preparation_method;
CREATE TABLE taco.preparation_method (
	"uuid" uuid NOT NULL,
	dish_uuid uuid NOT NULL,
	preparation_method text NOT NULL,
	CONSTRAINT preparation_method_pk PRIMARY KEY (uuid),
	CONSTRAINT preparation_method_dishes_fk FOREIGN KEY (dish_uuid) REFERENCES taco.dishes("uuid") ON DELETE RESTRICT ON UPDATE RESTRICT
);


-- DROP TABLE taco.recipes;
CREATE TABLE taco.recipes (
	"uuid" uuid NOT NULL,
	dish_uuid uuid NOT NULL,
	nutritional_value_uuid uuid NOT NULL,
	quantity numeric NOT NULL,
	CONSTRAINT recipes_pk PRIMARY KEY (uuid),
	CONSTRAINT recipes_dishes_fk FOREIGN KEY (dish_uuid) REFERENCES taco.dishes("uuid") ON DELETE RESTRICT ON UPDATE RESTRICT,
	CONSTRAINT recipes_nutritional_values_fk FOREIGN KEY (nutritional_value_uuid) REFERENCES taco.nutritional_values("uuid") ON DELETE RESTRICT ON UPDATE RESTRICT
);
