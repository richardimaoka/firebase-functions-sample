# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn, firestore_fn
from firebase_admin import initialize_app, firestore
import google.cloud.firestore

initialize_app()
#
#
@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response("Hello world!")

@firestore_fn.on_document_created(document="messages/{pushId}")
def makeuppercase(
    event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None],
) -> None:
    """Listens for new documents to be added to /messages. If the document has
    an "original" field, creates an "uppercase" field containg the contents of
    "original" in upper case."""

    # Get the value of "original" if it exists.
    if event.data is None:
        return
    try:
        original = event.data.get("original")
    except KeyError:
        # No "original" field, so do nothing.
        return

    # Set the "uppercase" field.
    print(f"Uppercasing {event.params['pushId']}: {original}")
    upper = original.upper()
    event.data.reference.update({"uppercase": upper})