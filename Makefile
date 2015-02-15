DB_NAME = "nb"
DB_INIT_DUMP_FOLDER = "instance/db_init_dump/"

run:
	python run.py

save_init_dump:
	@read -p "Mongo username: " user; \
	read -p "Mongo password: " pwd; \
	mongodump -d $(DB_NAME) -o $(DB_INIT_DUMP_FOLDER) -u $$user -p $$pwd

load_init_dump:
	@read -p "Mongo username: " user; \
	read -p "Mongo password: " pwd; \
	cd $(DB_INIT_DUMP_FOLDER); \
	mongorestore $(DB_NAME) -u $$user -p $$pwd