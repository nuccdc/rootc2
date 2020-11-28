## Root C2 Messages

To communicate with the root C2, you must use the protobuf messages in `./protobuf`.

There are protobuf stubs for a couple languages now, but more may be added by adjusting the Makefile.

### Golang usage

```golang

import (
  "time"
  "github.com/nuccdc/rootc2/golang/messages"
)

fn main() {
  victims := make([]*messages.VictimStatus, 1)
  victims[0] = &messages.VictimStatus{
    Host: "ip",
    LastHeardFrom: time.Now(),
  }
  messages.C2Update{
    MalwareId: "mymalware",
    Victims: victims,
    Timestamp: *time.Now(),
  }
}

```

