CREATE TYPE "user_role" AS ENUM (
  'worker',
  'reviewer',
  'admin'
);

CREATE TYPE "request_status" AS ENUM (
  'created',
  'approved',
  'rejected',
  'done'
);

CREATE TABLE "users" (
  "id" varchar(12) PRIMARY KEY,
  "name" varchar(80) NOT NULL,
  "email" varchar(40) NOT NULL,
  "roles" user_role[] NOT NULL
);

CREATE TABLE "requests" (
  "id" SERIAL PRIMARY KEY,
  "creator" varchar(12),
  "reviewer" varchar(12),
  "bonus_type" varchar(40) NOT NULL,
  "description" text,
  "status" request_status,
  "date_created" timestamp NOT NULL DEFAULT now(),
  "date_changed" timestamp NOT NULL DEFAULT now(),
  "date_payment" timestamp
);

ALTER TABLE "requests" ADD FOREIGN KEY ("creator") REFERENCES "users" ("id");

ALTER TABLE "requests" ADD FOREIGN KEY ("reviewer") REFERENCES "users" ("id");

ALTER TABLE "users" ADD CONSTRAINT "roles_overflow" CHECK (array_length("roles", 1) <= 3);

ALTER TABLE "requests" ADD CONSTRAINT "exclude_self_request" CHECK ("creator" <> "reviewer");