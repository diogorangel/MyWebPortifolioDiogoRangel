import pandas as pd
import numpy as np

# Dados fornecidos diretamente na sua solicitação (substitui a leitura do CSV para este exemplo)
# Se você tiver um arquivo CSV/Excel, use df = pd.read_csv('your_file.csv')
data = {
    'fname': ['Vincent', np.nan, np.nan, np.nan, 'Rembrandt', np.nan, np.nan, 'Leonardo', np.nan, np.nan, np.nan, 'Venture', np.nan, np.nan, 'Deborah', np.nan, 'Claude', np.nan, 'Pablo', np.nan, 'Michelangelo', np.nan],
    'mname': [np.nan, np.nan, np.nan, np.nan, 'Harmenszoon', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 'Lonzo', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 'di Lodovico', np.nan],
    'lname': ['van Gogh', np.nan, np.nan, np.nan, 'van Rijn', np.nan, np.nan, 'da Vinci', np.nan, np.nan, np.nan, 'Coy', np.nan, np.nan, 'Gill', np.nan, 'Monet', np.nan, 'Picasso', np.nan, 'Simoni', np.nan],
    'dob': [1853, np.nan, np.nan, np.nan, 1606, np.nan, np.nan, 1452, np.nan, np.nan, np.nan, 1965, np.nan, np.nan, 1970, np.nan, 1840, np.nan, 1904, np.nan, 1475, np.nan],
    'dod': [1890, np.nan, np.nan, np.nan, 1669, np.nan, np.nan, 1519, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 1926, np.nan, 1973, np.nan, 1564, np.nan],
    'country': ['France', np.nan, np.nan, np.nan, 'Netherlands', np.nan, np.nan, 'Italy', np.nan, np.nan, np.nan, 'United States', np.nan, np.nan, 'United States', np.nan, 'France', np.nan, 'Spain', np.nan, 'Italy', np.nan],
    'local': ['n', np.nan, np.nan, np.nan, 'n', np.nan, np.nan, 'n', np.nan, np.nan, np.nan, 'y', np.nan, np.nan, 'y', np.nan, 'n', np.nan, 'n', np.nan, 'n', np.nan],
    'title': [np.nan, 'Irises', 'The Starry Night', 'Sunflowers', np.nan, 'Night Watch', 'Storm on the Sea of Galilee', np.nan, 'Head of a Woman', 'Last Supper', 'Mona Lisa', np.nan, 'Hillside Stream', 'Old Barn', np.nan, 'Beach Baby', np.nan, 'Women in the Garden', np.nan, 'Old Guitarist', np.nan, np.nan],
    'year': [np.nan, 1889, 1889, 1888, np.nan, 1642, 1633, np.nan, 1508, 1498, 1517, np.nan, 2005, 1992, np.nan, 1999, np.nan, 1866, np.nan, 1904, np.nan, np.nan],
    'period': [np.nan, 'Impressionism', 'Post-Impressionism', 'Post-impressionism', np.nan, 'Baroque', 'Dutch Golden Age', np.nan, 'High Renaissance', 'Renaissance', 'Renaissance', np.nan, 'Modern', 'Modern', np.nan, 'Modern', np.nan, 'Impressionism', np.nan, 'Modern', np.nan, np.nan],
    'type': [np.nan, 'Oil', 'Oil', 'Oil', np.nan, 'Oil', 'Oil', np.nan, 'Oil', 'Tempra', 'Oil', np.nan, 'Oil', 'Oil', np.nan, 'Watercolor', np.nan, 'Oil', np.nan, 'Oil', np.nan, np.nan],
    'file': [np.nan, 'irises.jpg', 'starrynight.jpg', 'sunflowers.jpg', np.nan, 'nightwatch.jpg', 'stormgalilee.jpg', np.nan, 'headwoman.jpg', 'lastsupper.jpg', 'monalisa.jpg', np.nan, 'hillsidestream.jpg', 'oldbarn.jpg', np.nan, 'beachbaby.jpg', np.nan, 'womengarden.jpg', np.nan, 'guitarist.jpg', np.nan, np.nan],
    'keyword': [np.nan, 'flowers', 'blue, landscape', 'flowers', np.nan, 'girl, people, battle', 'boat, water, people, Christ', np.nan, 'girl, people', 'food, people, Christ', 'girl, people', np.nan, 'water, landscape', 'landscape', np.nan, 'water, people, baby', np.nan, 'landscape, people, flowers', np.nan, 'blue, people', np.nan, np.nan]
}
df = pd.DataFrame(data)


# --- Estruturas de dados para armazenar dados processados ---
artists_data = []  # Lista de dicionários para a tabela artist
artworks_data = []  # Lista de dicionários para a tabela artwork
keywords_data = []  # Lista de dicionários para a tabela keyword
keybridges_data = []  # Lista de dicionários para a tabela keybridge

# --- Mapeamentos para IDs ---
artist_name_to_id = {}  # Mapeia 'Nome do Artista' -> artist_id
keyword_to_id = {}      # Mapeia 'string_da_palavra_chave' -> keyword_id

# --- Contadores para IDs (simulando AUTO_INCREMENT) ---
current_artist_id = 1
current_artwork_id = 1
current_keyword_id = 1

# --- Variáveis temporárias para rastrear o artista atual ---
current_artist_in_loop_id = None

# --- Processar linhas do DataFrame ---
for index, row in df.iterrows():
    # Verificar se é uma linha de artista (baseado em 'fname' não ser NaN)
    if pd.notna(row['fname']):
        fname = str(row['fname']).strip() if pd.notna(row['fname']) else ''
        mname = str(row['mname']).strip() if pd.notna(row['mname']) else ''
        lname = str(row['lname']).strip() if pd.notna(row['lname']) else ''
        country = str(row['country']).strip() if pd.notna(row['country']) else ''

        # Construir o nome completo do artista
        artist_parts = [fname]
        if mname:
            artist_parts.append(mname)
        if lname:
            artist_parts.append(lname)
        full_artist_name = ' '.join(artist_parts).strip()

        if full_artist_name and full_artist_name not in artist_name_to_id:
            artists_data.append({
                'artist_id': current_artist_id,
                'artist_name': full_artist_name,
                'country': country
            })
            artist_name_to_id[full_artist_name] = current_artist_id
            current_artist_in_loop_id = current_artist_id
            current_artist_id += 1
        elif full_artist_name:
            current_artist_in_loop_id = artist_name_to_id[full_artist_name] # Usar ID existente


    # Verificar se é uma linha de obra de arte (baseado em 'title' não ser NaN)
    if pd.notna(row['title']) and current_artist_in_loop_id is not None:
        title = str(row['title']).replace("'", "''").strip()
        year = int(row['year']) if pd.notna(row['year']) else 'NULL'
        period = str(row['period']).replace("'", "''").strip() if pd.notna(row['period']) else 'NULL'
        artwork_type = str(row['type']).replace("'", "''").strip() if pd.notna(row['type']) else 'NULL'
        file_name = str(row['file']).strip() if pd.notna(row['file']) else 'NULL'
        keywords_str = str(row['keyword']).strip() if pd.notna(row['keyword']) else ''

        artworks_data.append({
            'artwork_id': current_artwork_id,
            'artist_id': current_artist_in_loop_id,
            'title': title,
            'year': year,
            'period': period,
            'description': 'NULL',  # O arquivo plano não tem descrição
            'type': artwork_type,
            'location': 'NULL',     # O arquivo plano não tem localização
            'donated': 'NULL',      # O arquivo plano não tem status de doação
            'file': file_name
        })

        # Processar palavras-chave para a obra de arte atual
        if keywords_str:
            # Dividir por vírgula, limpar espaços em branco e remover strings vazias
            individual_keywords = [k.strip() for k in keywords_str.split(',') if k.strip()]
            for keyword in individual_keywords:
                keyword_escaped = keyword.replace("'", "''")
                if keyword_escaped not in keyword_to_id:
                    keywords_data.append({
                        'keyword_id': current_keyword_id,
                        'keyword': keyword_escaped
                    })
                    keyword_to_id[keyword_escaped] = current_keyword_id
                    current_keyword_id += 1

                # Adicionar entrada à tabela keybridge
                keybridges_data.append({
                    'artwork_id': current_artwork_id,
                    'keyword_id': keyword_to_id[keyword_escaped]
                })

        current_artwork_id += 1

# --- Gerar instruções INSERT ---

insert_statements = []

# Instruções INSERT para a tabela Artist
insert_statements.append("-- INSERT statements for `artist` table")
for artist in artists_data:
    insert_statements.append(
        f"INSERT INTO `artist` (`artist_id`, `artist_name`, `country`) VALUES ({artist['artist_id']}, '{artist['artist_name']}', '{artist['country']}');"
    )

# Instruções INSERT para a tabela Artwork
insert_statements.append("\n-- INSERT statements for `artwork` table")
for artwork in artworks_data:
    # Lidar com NULLs para year, period, type, description, location, donated
    year_val = f"{artwork['year']}" if artwork['year'] != 'NULL' else "NULL"
    period_val = f"'{artwork['period']}'" if artwork['period'] != 'NULL' else "NULL"
    type_val = f"'{artwork['type']}'" if artwork['type'] != 'NULL' else "NULL"
    description_val = f"'{artwork['description']}'" if artwork['description'] != 'NULL' else "NULL"
    location_val = f"'{artwork['location']}'" if artwork['location'] != 'NULL' else "NULL"
    donated_val = f"{'TRUE' if artwork['donated'] else 'FALSE'}" if artwork['donated'] != 'NULL' else "NULL"
    file_val = f"'{artwork['file']}'" if artwork['file'] != 'NULL' else "NULL"

    insert_statements.append(
        f"INSERT INTO `artwork` (`artwork_id`, `artist_id`, `title`, `year`, `period`, `description`, `type`, `location`, `donated`, `file`) VALUES ("
        f"{artwork['artwork_id']}, "
        f"{artwork['artist_id']}, "
        f"'{artwork['title']}', "
        f"{year_val}, "
        f"{period_val}, "
        f"{description_val}, "
        f"{type_val}, "
        f"{location_val}, "
        f"{donated_val}, "
        f"{file_val}"
        f");"
    )

# Instruções INSERT para a tabela Keyword
insert_statements.append("\n-- INSERT statements for `keyword` table")
for keyword in keywords_data:
    insert_statements.append(
        f"INSERT INTO `keyword` (`keyword_id`, `keyword`) VALUES ({keyword['keyword_id']}, '{keyword['keyword']}');"
    )

# Instruções INSERT para a tabela Keybridge
insert_statements.append("\n-- INSERT statements for `keybridge` table")
for keybridge in keybridges_data:
    insert_statements.append(
        f"INSERT INTO `keybridge` (`artwork_id`, `keyword_id`) VALUES ({keybridge['artwork_id']}, {keybridge['keyword_id']});"
    )

# --- Montar o script SQL completo ---
sql_script_header = """
-- SQL Code for Database Creation (Forward Engineering)
-- Database: `art_gallery`

CREATE DATABASE IF NOT EXISTS `art_gallery`;
USE `art_gallery`;

-- Table `artist`
CREATE TABLE IF NOT EXISTS `artist` (
    `artist_id` INT NOT NULL AUTO_INCREMENT,
    `artist_name` VARCHAR(255) NOT NULL,
    `country` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`artist_id`)
) ENGINE = InnoDB;

-- Table `artwork`
CREATE TABLE IF NOT EXISTS `artwork` (
    `artwork_id` INT NOT NULL AUTO_INCREMENT,
    `artist_id` INT NOT NULL,
    `title` VARCHAR(255) NOT NULL,
    `year` INT,
    `period` VARCHAR(255),
    `description` TEXT,
    `type` VARCHAR(255),
    `location` VARCHAR(255),
    `donated` BOOLEAN,
    `file` VARCHAR(255),
    PRIMARY KEY (`artwork_id`),
    INDEX `fk_artwork_artist1_idx` (`artist_id` ASC) VISIBLE,
    CONSTRAINT `fk_artwork_artist1`
        FOREIGN KEY (`artist_id`)
        REFERENCES `art_gallery`.`artist` (`artist_id`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Table `keyword`
CREATE TABLE IF NOT EXISTS `keyword` (
    `keyword_id` INT NOT NULL AUTO_INCREMENT,
    `keyword` VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY (`keyword_id`)
) ENGINE = InnoDB;

-- Table `keybridge` (Linking table for Artwork and Keyword)
CREATE TABLE IF NOT EXISTS `keybridge` (
    `artwork_id` INT NOT NULL,
    `keyword_id` INT NOT NULL,
    PRIMARY KEY (`artwork_id`, `keyword_id`),
    INDEX `fk_keybridge_artwork1_idx` (`artwork_id` ASC) VISIBLE,
    INDEX `fk_keybridge_keyword1_idx` (`keyword_id` ASC) VISIBLE,
    CONSTRAINT `fk_keybridge_artwork1`
        FOREIGN KEY (`artwork_id`)
        REFERENCES `art_gallery`.`artwork` (`artwork_id`)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    CONSTRAINT `fk_keybridge_keyword1`
        FOREIGN KEY (`keyword_id`)
        REFERENCES `art_gallery`.`keyword` (`keyword_id`)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
) ENGINE = InnoDB;
"""

final_sql_script = sql_script_header + "\n" + "\n".join(insert_statements)

# Salvar em um arquivo SQL
with open("art_gallery_model_and_data.sql", "w") as f:
    f.write(final_sql_script)

print("Script SQL completo gerado com sucesso e salvo em 'art_gallery_model_and_data.sql'")