BEGIN;
CREATE TABLE "tmpls_types_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "description" varchar(300) NULL,
    "layout" varchar(1000) NOT NULL
)
;

CREATE TABLE "tmpls_template_users" (
    "id" integer NOT NULL PRIMARY KEY,
    "template_id" integer NOT NULL REFERENCES "tmpls_template" ("id"),
    "user_id" integer NULL REFERENCES "auth_user" ("id"),
    UNIQUE ("template_id", "user_id")
)
;
CREATE TABLE "tmpls_template" (
    "id" integer NOT NULL PRIMARY KEY,
    "templateType_id" integer NOT NULL REFERENCES "tmpls_types_type" ("id"),
    "name" varchar(300) NOT NULL,
    "isPublish" bool NOT NULL,
    "isPublic" bool NOT NULL
)
;

COMMIT;