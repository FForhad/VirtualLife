from rest_framework.response import Response

def generate_response(success: bool, message: str, status: int, data=None) -> Response:
    response_data = {
        'success': success,
        'message': message,
        'status': status,
    }
    
    if data is not None:
        response_data['data'] = data

    return Response(response_data, status=status)
