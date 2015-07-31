# http://jsonschema.net/

'''
{
  "anchor": {
    "unsigned": "{hex}"
  },
  "refund": {
    "unsigned": "{hex}"
  },
  "params": {
    "sats_per_update": 600,
    "master_pub": "{hex}"
  }
}
'''
create_channel = {
  "id": "",
  "type": "object",
  "properties": {
    "anchor": {
      "id": "/anchor",
      "type": "object",
      "properties": {
        "unsigned": {
          "id": "/anchor/unsigned",
          "type": "string"
        }
      },
      "additionalProperties": False,
      "required": [
        "unsigned"
      ]
    },
    "refund": {
      "id": "/refund",
      "type": "object",
      "properties": {
        "unsigned": {
          "id": "/refund/unsigned",
          "type": "string"
        }
      },
      "additionalProperties": False,
      "required": [
        "unsigned"
      ]
    },
    "params": {
      "id": "/params",
      "type": "object",
      "properties": {
        "sats_per_update": {
          "id": "/params/sats_per_update",
          "type": "integer"
        },
        "master_pub": {
          "id": "/params/master_pub",
          "type": "string"
        }
      },
      "additionalProperties": False,
      "required": [
        "sats_per_update",
        "master_pub"
      ]
    }
  },
  "additionalProperties": False,
  "required": [
    "anchor",
    "refund",
    "params"
  ]
}