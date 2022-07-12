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

CREATE TABLE "user" (
  "id" character(12) PRIMARY KEY,
  "name" character(80) NOT NULL,
  "email" character(40) NOT NULL,
  "roles" user_role[] NOT NULL
);

CREATE TABLE "request" (
  "id" SERIAL PRIMARY KEY,
  "creator" character(12),
  "reviewer" character(12),
  "bonus_type" character(40) NOT NULL,
  "description" text
);

CREATE TABLE "request_history" (
  "request_id" int PRIMARY KEY,
  "status" request_status NOT NULL DEFAULT 'created',
  "date_created" timestamp NOT NULL,
  "date_approved" timestamp,
  "date_rejected" timestamp,
  "date_done" timestamp,
  "date_changed" timestamp,
  "date_payment" timestamp
);

ALTER TABLE "request" ADD FOREIGN KEY ("creator") REFERENCES "user" ("id");

ALTER TABLE "request" ADD FOREIGN KEY ("reviewer") REFERENCES "user" ("id");

ALTER TABLE "request_history" ADD FOREIGN KEY ("request_id") REFERENCES "request" ("id");

ALTER TABLE "user" ADD CONSTRAINT "roles_overflow" CHECK (array_length("roles", 1) <= 3);

ALTER TABLE "request" ADD CONSTRAINT "exclude_self_request" CHECK ("creator" <> "reviewer");

ALTER TABLE "request_history" ADD CONSTRAINT "exclude_opposite_status" CHECK (NOT ("date_approved" IS NOT NULL AND "date_rejected" IS NOT NULL));