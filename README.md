# Personregister i testmiljön

Detta projekt demonstrerar hur testdata kan hanteras på ett GDPR-kompatibelt sätt i en isolerad testmiljö.  
Systemet använder Python, SQLite och Docker för att lagra, visa, anonymisera och rensa testdata.

Projektet visar också hur CI/CD kan användas med GitHub Actions för att automatiskt verifiera koden.

---

# Funktioner

Systemet innehåller följande funktioner:

- Skapa syntetiska testanvändare i en SQLite-databas
- Visa innehållet i databasen
- Anonymisera användardata enligt GDPR
- Rensa testdata från databasen
- Köra systemet i en Docker-container
- Automatisk build via GitHub Actions

---

# Tekniker som används

- Python
- SQLite
- Docker
- Docker Compose
- Git & GitHub
- GitHub Actions (CI/CD)
- Jira (SAFe projektplanering)

---

# Installation

## Klona repository

```bash
git clone https://github.com/AliReza-Hezareh/personregister-testmiljo
cd personregister-testmiljo
```
### Köra i terminalen

köra docker
docker-compose up --build
----------------------------------------------------------------------------------------------------------------------
annonymisering
docker exec gdpr-user-registry python -c "import app; app.anonymize_user(); app.display_users()"
----------------------------------------------------------------------------------------------------------------------
rensa data
docker exec gdpr-user-registry python -c "import app; app.clear_test_data(); app.display_users()"
----------------------------------------------------------------------------------------------------------------------
Det stoppar containern.
CTRL + C
----------------------------------------------------------------------------------------------------------------------
Stoppa gamla containers
docker compose down
----------------------------------------------------------------------------------------------------------------------
Starta container igen utan rebuild
docker compose up
----------------------------------------------------------------------------------------------------------------------
se vilka container som körs
docker ps
----------------------------------------------------------------------------------------------------------------------
se alla containers
docker ps -a
----------------------------------------------------------------------------------------------------------------------
se loggar från containern
docker logs gdpr-user-registry
----------------------------------------------------------------------------------------------------------------------
köra kommandon inne i containern
docker exec -it gdpr-user-registry bash
python direkt
docker exec -it gdpr-user-registry python
----------------------------------------------------------------------------------------------------------------------
ta bort allt från docker compose 
docker compose down -v
----------------------------------------------------------------------------------------------------------------------