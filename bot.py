import requests
def get_access_token():
    """Gets the access token for the currently logged in user.

    Returns:
        str: The access token.
    """

    # Create the authorization header.
    authorization = "Basic Electrical_Jogi_392:Seeker16@"

    # Make the request to the Reddit API.
    response = requests.post("https://api.reddit.com/api/v1/access_token", headers={"Authorization": authorization})

    # Parse the response.
    data = response.json()
    print(data)
    return data["access_token"]
def place_pixel(color, x, y):
    """Places a pixel on the r/place canvas.

    Args:
        color (str): The color of the pixel.
        x (int): The x-coordinate of the pixel.
        y (int): The y-coordinate of the pixel.
    """
    

    url = "https://api.reddit.com/place/canvas_pixel"
    data = {
        "color": color,
        "x": x,
        "y": y,
    }

    # Create the authorization header.
    authorization = "Bearer <access token>"

    # Add the authorization header to the request.
    response = requests.post(url, data=data, headers={"Authorization": authorization})

    if response.status_code == 200:
        print("Successfully placed pixel at (x, y) = ({}, {})".format(x, y))
    else:
        print("Failed to place pixel at (x, y) = ({}, {})".format(x, y))

if __name__ == "__main__":
    # Get the access token from the environment.
    access_token = get_access_token()
    print(access_token)
#    access_token = os.environ["REDDIT_ACCESS_TOKEN"]
#
#    # Set the color of the pixel.
#    color = "#ffffff"
#
#    # Set the x-coordinate of the pixel.
#    x = 0
#
#    # Set the y-coordinate of the pixel.
#    y = 0
#
#    # Place the pixel.
#    place_pixel(color, x, y)
