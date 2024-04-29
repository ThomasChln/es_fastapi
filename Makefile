
all:
	docker compose up --build index
	docker compose up --build -d app

clean:
	docker rm -f es_fastapi-index-1 es_fastapi-app-1 es_fastapi-es-1
	docker volume rm es_fastapi_esdata

download:
	wget -O app/epmc_suic_ftext.json "https://www.dropbox.com/scl/fi/c7hfa1iutz2ertzec5gp4/epmc_suic_ftext.json?rlkey=tiw3x9zehunvmhfpstbald7il&st=o8tkgdvd&dl=0"

