#!/bin/bash

HOOKS=(pre-commit commit-msg prepare-commit-msg)

# Adds the call to the local hook files to the .git/hooks commands
# Creates the .git/hooks commands if they don't already exists
for HOOK in ${HOOKS[@]}
do
  HOOK_FILE=.git/hooks/${HOOK}
  HOOK_CMD="scripts/${HOOK}.sh"

  if [ -f $HOOK_FILE ]; then
      if ! grep -q "$HOOK_CMD" "$HOOK_FILE"; then
          echo "" >> $HOOK_FILE
          echo $HOOK_CMD >> $HOOK_FILE
      fi
  else
      echo "#!/bin/bash" > $HOOK_FILE
      echo "" >> $HOOK_FILE
      echo $HOOK_CMD >> $HOOK_FILE
      chmod +x $HOOK_FILE
  fi

done

ALLOWED_KEYS=(01222222222222222222 03333333333333333333 02222222222222222222 MSLOSTPOINTERCAPTURE)
for ALLOWED_KEY in ${ALLOWED_KEYS[@]}
do
  git config --get-all secrets.allowed | grep ${ALLOWED_KEY} --silent
  if [ $? -ne 0 ]; then
    git config --add secrets.allowed ${ALLOWED_KEY}
  fi

done

