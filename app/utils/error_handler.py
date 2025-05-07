from flask import jsonify
from werkzeug.exceptions import HTTPException

def init_error_handling(app):

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Handle HTTP Exception"""
        app.logger.error(f"HTTP Exception occurred: {str(e)}")
        return jsonify({
            "error": e.name,
            "message": e.description
        }), e.code
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        """Handle Unexpected error"""
        app.logger.error(f"Unexpected error occurred: {str(e)}")
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

    @app.errorhandler(AttributeError)
    def handle_attribute_error(e):
        """Handle Attribute error"""
        app.logger.error(f"Attribute error occurred: {str(e)}")
        return jsonify({
            "error": "Attribute Error",
            "message": str(e)
        }), 500
    
    @app.errorhandler(404)
    def handle_not_found(e):
        app.logger.warning(f"Resource not found: {e}")
        return jsonify({
            "error": "Not found",
            "message": "Resource you requested could not be found"
        }), 404
    
    @app.errorhandler(400)
    def handle_bad_request(e):
        """Handle 400 Bad Request error."""
        app.logger.warning(f"Bad request: {e}")
        return jsonify({
            "error": "Bad Request",
            "message": "The request is malformed or missing required parameters."
        }), 400
    