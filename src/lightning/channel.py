from enum import Enum
from lightning import exceptions as E

#
# Channel classes
#

class ChannelState(Enum):
  START = 0
  REFUND_ESTABLISHED = 1
  ANCHOR_POSTED = 2

class ChannelParams:
  def __init__(self, anchor_txid, sats_per_update):
    # Anchor txid hash
    self.anchor_txid = anchor_txid
    # Channel updates happen this many satoshis at a time
    self.sats_per_update = sats_per_update

class Channel:
  def __init__(self, channel_state, channel_params):
    self.channel_state = channel_state
    self.channel_params = channel_params

#
# Channel functions
#

def create_channel(request):
  raise E.ChannelRequestError('Not implemented yet.')

def read_channel(request):
  raise E.ChannelRequestError('Not implemented yet.')

def update_channel(request):
  raise E.ChannelRequestError('Not implemented yet.')

def destroy_channel(request):
  raise E.ChannelRequestError('Not implemented yet.')

def refresh_channel(request):
  raise E.ChannelRequestError('Not implemented yet.')


