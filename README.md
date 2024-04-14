## Blog API using Django REST Framework

This project showcases my proficiency in building robust RESTful APIs using Django REST Framework. The Blog API is designed to manage and interact with blog content through HTTP endpoints.

### Features:
- **Authentication**: Utilizes `djangorestframework-simplejwt` for secure authentication, ensuring that only authorized users can access protected endpoints.
- **Cross-Origin Resource Sharing (CORS)**: Integrates `corsheaders` to handle Cross-Origin Resource Sharing, allowing client-side applications hosted on different domains to interact with the API.
- **API Documentation**: Utilizes `drf-yasg` to generate interactive API documentation using Swagger, providing clear and comprehensive documentation for API endpoints.
- **CRUD Operations**: Implements CRUD (Create, Read, Update, Delete) operations to manage blog posts, enabling users to create, retrieve, update, and delete blog content via the API.
- **Customization**: Demonstrates the ability to customize serializers, views, and models to meet specific project requirements and business logic.
- **Versioning**: Supports API versioning to manage changes and updates to the API endpoints effectively.

### Technologies Used:
- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs in Django.
- **djangorestframework-simplejwt**: A JSON Web Token (JWT) authentication plugin for Django REST Framework.
- **corsheaders**: Django application for handling Cross-Origin Resource Sharing (CORS).
- **drf-yasg**: Yet Another Swagger Generator for Django REST Framework, used for API documentation.

### Usage:
- Clone the repository: `git clone https://github.com/mrted/blog_project`
- Install dependencies: `pipenv update`
- Create a `.env` file in the root directory of the project and your environment variables. See `.env.example` for an example.
- Apply database migrations: `python manage.py migrate`
- Run the development server: `python manage.py runserver`

### Documentation:
- Access the API documentation: [Swagger UI](http://localhost:8000/swagger/) or [Redoc](http://localhost:8000/redoc/)

### Contributions:
Contributions and feedback are welcome! Feel free to open issues or pull requests for any improvements or suggestions.


