from external_api import ExternalRESTAPI
from adapter import APIAdapter
from decorator import auth_required

@auth_required
def api_handler(user_authenticated):
    print("Accessing Secure API Handler")


def main():
    print("=== Adapter Pattern ===")
    external_api = ExternalRESTAPI()
    adapter = APIAdapter(external_api)
    user = adapter.get_user()
    print(user)

    print("\n=== Decorator Pattern ===")

    print("\nCase 1: Authenticated User")
    api_handler(True)

    print("\nCase 2: Unauthenticated User")
    api_handler(False)

if __name__ == "__main__":
    main()