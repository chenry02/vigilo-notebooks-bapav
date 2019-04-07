UID=$(shell id -u)
IMAGE_VERSION=65761486d5d3
PACKAGES=ipyleaflet requests pandas matplotlib seaborn overpy geopy
all: help

help:
	@grep "##" Makefile | grep -v "@grep"


.conda:
	docker exec jupyter conda install -y -c conda-forge ${PACKAGES}

.npm: ## Install .virtualenv
	docker exec jupyter jupyter labextension install jupyter-leaflet @jupyter-widgets/jupyterlab-manager

run: ## Run docker container
	docker run -d --name jupyter --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "${CURDIR}":/home/jovyan jupyter/datascience-notebook:${IMAGE_VERSION}

jupyter: stop run .conda .npm ## Launch jupyter instance
	@echo "#########################################################"
	@echo "# You can now launch your web navigator to localhost:8888" 
	@echo "#########################################################"


stop: ## stop jupyter docker container
	@docker stop jupyter > /dev/null || true
	@echo "Stoping or waiting jupyter container" && sleep 5
	@docker rm jupyter > /dev/null || true

clean: ## Clean packages installation
	-@$(RM) -r .cache
	-@$(RM) -r .conda
	-@$(RM) -r .config
	-@$(RM) -r .ipy*
	-@$(RM) -r .local
	-@$(RM) -r .npm
	-@$(RM) -r .yarn
	-@$(RM) -r .yarnrc
	-@$(RM) -r .requirements





