from bottle import Bottle, run, request, abort
from lightning import channel
from lightning import exceptions as E
from jsonschema import validate, ValidationError
import schema

# This is a basic API controller class
# that does little more than define the routes
# and make calls to lightning methods

app = Bottle()

@app.route('/channel', 'POST')
def create_channel():
  '''
  Request to open a new channel with this node.
  Request may certainly be denied.
  '''
  try:
    validate(request.json, schema.create_channel)
    return channel.create_channel(request.json)
  except ValidationError as e:
    abort(400, str(e))
  except E.ChannelRequestError as e:
    abort(400, str(e))
  except ValueError as e:
    abort(400, str(e))

@app.route('/channel', 'GET')
def read_channel():
  '''
  Read channel status.
  If proof of ownership of the channel key is given, then more
  detailed information will be given.
  Without proof of ownership of the channel key, limited information
  will be given.
  '''
  try:
    return channel.read_channel(request.json)
  except ValidationError as e:
    abort(400, str(e))
  except E.ChannelRequestError as e:
    abort(400, str(e))
  except ValueError as e:
    abort(400, str(e))

@app.route('/channel', 'PATCH')
def update_channel():
  '''
  Make a payment on a channel.
  An alternate type of patch is to
  '''
  try:
    return channel.update_channel(request.json)
  except ValidationError as e:
    abort(400, str(e))
  except E.ChannelRequestError as e:
    abort(400, str(e))
  except ValueError as e:
    abort(400, str(e))

@app.route('/channel', 'DELETE')
def destroy_channel():
  '''
  Close out a channel.
  '''
  try:
    return channel.destroy_channel(request.json)
  except ValidationError as e:
    abort(400, str(e))
  except E.ChannelRequestError as e:
    abort(400, str(e))
  except ValueError as e:
    abort(400, str(e))

@app.route('/channel', 'PUT')
def refresh_channel():
  '''
  Request to refresh a channel early, posting
  the net transactions to the blockchain early.
  Request may be refused.
  '''
  try:
    return channel.refresh_channel(request.json)
  except ValidationError as e:
    abort(400, str(e))
  except E.ChannelRequestError as e:
    abort(400, str(e))
  except ValueError as e:
    abort(400, str(e))

# Use 0.0.0.0 since running in docker VM
run(app, host="0.0.0.0", port=8090, debug=True)
