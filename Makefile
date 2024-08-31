MAKEFLAGS+="-j 2"

init:
	pip install -r requirements.txt
	@pnpm --prefix "vite" install

dev-python:
	flask --debug run

dev-vue:
	flask vite start

dev: dev-python dev-vue

prod-python:
	echo "You must implement your production service here"
	exit 1

prod-vue:
	@flask vite build

prod: prod-vue prod-python
