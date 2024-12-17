
#!/bin/bash

set  -e

wandb  login $WANDB_Token
exec "$@"
