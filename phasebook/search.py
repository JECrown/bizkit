from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")

def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!        

    matching_users = []
    seen_ids = []

    if args.get("id") is not None:
        for user in USERS:
            if user["id"] == args.get("id"):
                if user["id"] not in seen_ids:
                    matching_users.append(user)
                    seen_ids.append(user["id"])
                break

    if args.get("name") is not None:
        for user in USERS:
            if args.get("name").lower() in user["name"].lower():
                if user["id"] not in seen_ids:
                    matching_users.append(user)
                    seen_ids.append(user["id"])

    if args.get("age") is not None:
        for user in USERS:
            if user["age"] != 0 and int(args.get("age")) - 1 <= user["age"] <= int(args.get("age")) + 1:
                if user["id"] not in seen_ids:
                    matching_users.append(user)
                    seen_ids.append(user["id"])

    if args.get("occupation") is not None:
        for user in USERS:
            if args.get("occupation").lower() in user["occupation"].lower():
                if user["id"] not in seen_ids:
                    matching_users.append(user)
                    seen_ids.append(user["id"])


    return matching_users




