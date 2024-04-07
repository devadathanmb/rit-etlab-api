from flasgger import Swagger

from app import create_app
from app.docs.swagger import swagger_config

app = create_app()
Swagger(app, config=swagger_config)

if __name__ == "__main__":
    app.run(debug=True)
