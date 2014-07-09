package fkp

import (
	zmq "github.com/pebbe/zmq4"
	"log"
)

type FKServer struct {
	Sock *zmq.Socket
}

func NewFKServer(file string) FKServer {
	s, _ := zmq.NewSocket(zmq.REP)
	s.Bind("ipc:///tmp/fk/" + file)

	c := FKServer{
		Sock: s,
	}
	go c.ParserLoop()

	return c
}

func (s *FKServer) ParserLoop() {
	for {
		data, e := s.Sock.RecvBytes(0)
		if e != nil {
			break
		}
		log.Printf("::%v", data)
	}
}
