                    from prometheus_client import Counter, Histogram, generate_latest

                    from flask import Response, request

                    import time



                    # Initialize Prometheus metrics

                    REQUEST_COUNT = Counter('flask_app_request_count', 'Number of requests', ['method', 'endpoint', 'http_status'])

                    REQUEST_LATENCY = Histogram('flask_app_request_latency_seconds', 'Request latency', ['method', 'endpoint'])



                    # Middleware to track request metrics

                    def before_request():

                        request.start_time = time.time()



                    def after_request(response):

                        request_latency = time.time() - request.start_time

                        REQUEST_LATENCY.labels(request.method, request.path).observe(request_latency)

                        REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()

                        return response



                    # Expose Prometheus metrics endpoint

                    def metrics():

                        return Response(generate_latest(), mimetype='text/plain')



                    # Register middleware and metrics endpoint in the Flask app

                    if __name__ == '__main__':

                        import connexion

                        from swagger_server import encoder



                        app = connexion.App(__name__, specification_dir='./swagger/')

                        flask_app = app.app

                        flask_app.json_encoder = encoder.JSONEncoder



                        # Register middleware

                        flask_app.before_request(before_request)
                        flask_app.after_request(after_request)
                        flask_app.add_url_rule('/metrics', 'metrics', metrics)
                        app.add_api('swagger.yaml', arguments={'title': 'Flask App with Prometheus Metrics'})

                        app.run(port=8080)
