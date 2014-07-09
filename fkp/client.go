package fkp

import (
	zmq "github.com/pebbe/zmq4"
	"time"
)

type FKClient struct {
	Sock *zmq.Socket
}

func (c *FKClient) Init() {
	c.Sock.SendBytes(SerializePacket(
		&HelloPacket{
			ParentID:  1,
			SessionID: 1,
			ProtocolV: PROTOCOL_VERSION,
		}), 0)
	go c.ParserLoop()
}

func (c *FKClient) ParserLoop() {
	for {
		time.Sleep(time.Second)
	}
}

func NewFKClient(file string) FKClient {
	s, _ := zmq.NewSocket(zmq.REQ)
	s.Connect("ipc:///tmp/fk/" + file)
	c := FKClient{
		Sock: s,
	}

	time.Sleep(time.Second * 5)
	c.Init()
	return c
}
