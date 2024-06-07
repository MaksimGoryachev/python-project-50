install:
	poetry install
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 gendiff

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

setup: install build package-install
