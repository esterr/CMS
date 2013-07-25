BEGIN;
CREATE TABLE "tmpls_types_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "description" varchar(300) NOT NULL
)
;

CREATE TABLE "tmpls_template_users" (
    "id" integer NOT NULL PRIMARY KEY,
    "template_id" integer NOT NULL REFERENCES "tmpls_template" ("id"),
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    UNIQUE ("template_id", "user_id")
)
;
CREATE TABLE "tmpls_template1" (
    "id" integer NOT NULL PRIMARY KEY,
    "templateType_id" integer NOT NULL REFERENCES "tmpls_types_type" ("id"),
    "name" varchar(300) NOT NULL,
    "isPublish" bool NOT NULL,
    "isPublic" bool NOT NULL
)
;

INSERT INTO "tmpls_template1" SELECT id,templateType_id,name,isPublish,isPublic FROM "tmpls_template";

COMMIT;
BEGIN TRANSACTION;
CREATE TABLE "tmpls_template1" (
    "id" integer NOT NULL PRIMARY KEY,
    "templateType_id" integer NOT NULL REFERENCES "tmpls_types_type" ("id"),
    "name" varchar(300) NOT NULL,
    "content" varchar(500) NOT NULL,
    "isPublish" bool NOT NULL,
    "isPublic" bool NOT NULL
)
;
