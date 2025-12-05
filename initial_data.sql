-- Categorias (ayudado con ia)
INSERT INTO categories (name, description, created_at, updated_at) VALUES
('Ficción', 'Obras literarias de ficción narrativa', NOW(), NOW()),
('No Ficción', 'Obras basadas en hechos reales y documentados', NOW(), NOW()),
('Ciencia', 'Libros de divulgación y estudio científico', NOW(), NOW()),
('Historia', 'Obras históricas, cronológicas y biográficas', NOW(), NOW()),
('Fantasía', 'Narrativa fantástica, épica y mitológica', NOW(), NOW());

-- 5 Usuarios con informacion completa y contraseñas hasheadas usando argon2
INSERT INTO users (username, fullname, password, email, phone, address, is_active, created_at, updated_at) VALUES
('tcastillo', 'Tomás Castillo Vera', '$argon2id$v=19$m=65536,t=3,p=4$9mYH4xZD5wSfE9I5uxei9A$pL7kN3xQ8sM5uH2vJ9cF6dR4aY8bP1eT3gW6hU9nK0', 'tcastillo@biblioteca.cl', '+56947823156', 'Calle Chiloé 456, Punta Arenas', true, NOW(), NOW()),
('isanchez', 'Isabel Sánchez Pino', '$argon2id$v=19$m=65536,t=3,p=4$9mYH4xZD5wSfE9I5uxei9A$pL7kN3xQ8sM5uH2vJ9cF6dR4aY8bP1eT3gW6hU9nK0', 'isanchez@biblioteca.cl', '+56938156742', 'Av. Costanera 892, Punta Arenas', true, NOW(), NOW()),
('fmuñoz', 'Felipe Muñoz Jara', '$argon2id$v=19$m=65536,t=3,p=4$9mYH4xZD5wSfE9I5uxei9A$pL7kN3xQ8sM5uH2vJ9cF6dR4aY8bP1eT3gW6hU9nK0', 'fmunoz@biblioteca.cl', '+56925479813', 'Pasaje O Higgins 234, Punta Arenas', true, NOW(), NOW()),
('mnavia', 'Macarena Navia Lagos', '$argon2id$v=19$m=65536,t=3,p=4$9mYH4xZD5wSfE9I5uxei9A$pL7kN3xQ8sM5uH2vJ9cF6dR4aY8bP1eT3gW6hU9nK0', 'mnavia@biblioteca.cl', '+56951234689', 'Calle Angamos 567, Punta Arenas', true, NOW(), NOW()),
('eortiz', 'Eduardo Ortiz Bravo', '$argon2id$v=19$m=65536,t=3,p=4$9mYH4xZD5wSfE9I5uxei9A$pL7kN3xQ8sM5uH2vJ9cF6dR4aY8bP1eT3gW6hU9nK0', 'eortiz@biblioteca.cl', '+56964987235', 'Av. Manuel Señoret 789, Punta Arenas', true, NOW(), NOW());

-- 10 Libros distribuidos en categorias con ISBNs formato correspondiente
INSERT INTO books (title, author, isbn, pages, published_year, stock, description, language, publisher, created_at, updated_at) VALUES
('La sombra del viento', 'Carlos Ruiz Zafón', 'ISBN-BD2-2025-3847', 567, 2001, 6, 'Misterio literario en la Barcelona de posguerra', 'es', 'Planeta', NOW(), NOW()),
('Rayuela', 'Julio Cortázar', 'ISBN-BD2-2025-5129', 635, 1963, 4, 'Novela experimental sobre un intelectual argentino', 'es', 'Sudamericana', NOW(), NOW()),
('El gen egoísta', 'Richard Dawkins', 'ISBN-BD2-2025-7423', 368, 1976, 5, 'Perspectiva evolutiva centrada en los genes', 'es', 'Oxford University Press', NOW(), NOW()),
('Una breve historia de casi todo', 'Bill Bryson', 'ISBN-BD2-2025-8965', 544, 2003, 7, 'Viaje divulgativo por el conocimiento científico', 'es', 'Broadway Books', NOW(), NOW()),
('El universo en tu mano', 'Christophe Galfard', 'ISBN-BD2-2025-2614', 392, 2015, 4, 'Viaje por la física cuántica y la relatividad', 'es', 'Blackie Books', NOW(), NOW()),
('Guns, Germs, and Steel', 'Jared Diamond', 'ISBN-BD2-2025-4758', 480, 1997, 3, 'Factores que moldearon las civilizaciones', 'en', 'W.W. Norton', NOW(), NOW()),
('SPQR', 'Mary Beard', 'ISBN-BD2-2025-9183', 608, 2015, 5, 'Historia de la antigua Roma y su legado', 'es', 'Crítica', NOW(), NOW()),
('El nombre de la rosa', 'Umberto Eco', 'ISBN-BD2-2025-6347', 503, 1980, 6, 'Misterio medieval en una abadía italiana', 'es', 'Bompiani', NOW(), NOW()),
('La rueda del tiempo', 'Robert Jordan', 'ISBN-BD2-2025-1529', 782, 1990, 8, 'Épica fantasía con múltiples tramas entrelazadas', 'es', 'Tor Books', NOW(), NOW()),
('Mistborn: Nacidos de la bruma', 'Brandon Sanderson', 'ISBN-BD2-2025-8741', 541, 2006, 9, 'Sistema único de magia basado en metales', 'es', 'Tor Books', NOW(), NOW());

-- Relacion libros-categorias
INSERT INTO book_categories (book_id, category_id) VALUES
(1, 1), 
(2, 1), 
(3, 3), 
(4, 2), 
(4, 3), 
(5, 3), 
(6, 2), 
(6, 4), 
(7, 4), 
(8, 1), 
(8, 4), 
(9, 5), 
(10, 5);

-- 8 Prestamos variados 
INSERT INTO loans (loan_dt, return_dt, due_date, fine_amount, status, user_id, book_id, created_at, updated_at) VALUES
('2024-11-27', NULL, '2024-12-11', NULL, 'ACTIVE', 1, 2, NOW(), NOW()),
('2024-11-30', NULL, '2024-12-14', NULL, 'ACTIVE', 3, 5, NOW(), NOW()),
('2024-10-28', '2024-11-08', '2024-11-11', 0.00, 'RETURNED', 2, 3, NOW(), NOW()),
('2024-11-02', '2024-11-13', '2024-11-16', 0.00, 'RETURNED', 5, 7, NOW(), NOW()),
('2024-10-10', '2024-11-01', '2024-10-24', 4000.00, 'RETURNED', 4, 1, NOW(), NOW()), 
('2024-10-22', '2024-11-09', '2024-11-05', 2000.00, 'RETURNED', 1, 6, NOW(), NOW()),
('2024-11-08', NULL, '2024-11-22', NULL, 'ACTIVE', 2, 8, NOW(), NOW()),
('2024-11-14', NULL, '2024-11-28', NULL, 'ACTIVE', 4, 9, NOW(), NOW());

-- 15 Reseñas distribuidas entre libros y usuarios
INSERT INTO reviews (rating, comment, review_date, user_id, book_id, created_at, updated_at) VALUES
(5, 'Narrativa envolvente que atrapa desde el primer capítulo', '2024-11-12', 1, 1, NOW(), NOW()),
(4, 'Innovador pero requiere concentración para disfrutarlo', '2024-11-13', 2, 2, NOW(), NOW()),
(5, 'Cambió mi forma de entender la evolución', '2024-11-14', 3, 3, NOW(), NOW()),
(5, 'Divulgación científica en su mejor expresión', '2024-11-15', 4, 4, NOW(), NOW()),
(4, 'Conceptos complejos explicados de manera accesible', '2024-11-16', 5, 5, NOW(), NOW()),
(5, 'Perspectiva reveladora sobre el desarrollo humano', '2024-11-17', 1, 6, NOW(), NOW()),
(5, 'La mejor introducción a la historia romana', '2024-11-18', 2, 7, NOW(), NOW()),
(5, 'Mezcla perfecta de misterio, historia y filosofía', '2024-11-19', 3, 8, NOW(), NOW()),
(4, 'Inicio lento pero vale totalmente la pena', '2024-11-20', 4, 9, NOW(), NOW()),
(5, 'Sistema de magia más original que he leído', '2024-11-21', 5, 10, NOW(), NOW()),
(5, 'Zafón crea una atmósfera única e inolvidable', '2024-11-22', 2, 1, NOW(), NOW()),
(5, 'Dawkins explica ideas complejas con claridad', '2024-11-23', 4, 3, NOW(), NOW()),
(4, 'Exhaustivo y bien documentado', '2024-11-24', 1, 7, NOW(), NOW()),
(5, 'Suspense medieval magistralmente construido', '2024-11-25', 5, 8, NOW(), NOW()),
(5, 'Worldbuilding excepcional y personajes memorables', '2024-11-26', 3, 9, NOW(), NOW());