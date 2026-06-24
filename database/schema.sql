-- Schema futuro do OpsPilot AI
-- Este arquivo sera usado apenas na fase PostgreSQL.
-- Nao execute este script na fase inicial do projeto.

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(30),
    email VARCHAR(120),
    company_name VARCHAR(120),
    source VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id),
    title VARCHAR(150) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    status VARCHAR(50),
    urgency VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    request_id INTEGER REFERENCES requests(id),
    title VARCHAR(150) NOT NULL,
    status VARCHAR(50),
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ai_analyses (
    id SERIAL PRIMARY KEY,
    request_id INTEGER REFERENCES requests(id),
    category VARCHAR(80),
    urgency VARCHAR(50),
    summary TEXT,
    next_action TEXT,
    raw_result JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    event_type VARCHAR(80),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
