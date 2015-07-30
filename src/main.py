from bottle import Bottle, run

app = Bottle()
@app.route('/channel', 'POST')
def create_channel():
  """
  Request to open a new channel with this node.
  Request may certainly be denied.
  """
  return {}

@app.route('/channel', 'GET')
def read_channel():
  """
  Read channel status.
  If proof of ownership of the channel key is given, then more
  detailed information will be given.
  Without proof of ownership of the channel key, limited information
  will be given.
  """
  return {}

@app.route('/channel', 'PATCH')
def update_channel():
  """
  Make a payment on a channel.
  """
  return {}

@app.route('/channel', 'DELETE')
def destroy_channel():
  """
  Close out a channel.
  """
  return {}

@app.route('/channel', 'PUT')
def refresh_channel():
  """
  Request to refresh a channel early, posting
  the net transactions to the blockchain early.
  Request may be refused.
  """
  return {}

# Use 0.0.0.0 since running in docker VM
run(app, host="0.0.0.0", port=8090, debug=True)
