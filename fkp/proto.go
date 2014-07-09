package fkp

import (
	"bytes"
	"encoding/binary"
	"time"
)

func SerializePacket(p Packet) []byte {
	p.Build()
	buf := bytes.NewBufferString("")
	binary.Write(buf, binary.LittleEndian, p)
	return buf.Bytes()
}

type Packet interface {
	Build()
}

type BasePacket struct {
	ID   uint16
	When time.Time
}

func NewBasePacket(id uint16) BasePacket {
	return BasePacket{
		ID:   id,
		When: time.Now(),
	}
}

// Represents the inital handshaking packet
type HelloPacket struct {
	BasePacket

	// ParentID is the parent process ID
	ParentID uint16

	// SessionID is the current session ID as given by the parent.
	SessionID uint32

	// ProtocolV is the current protocol version.
	ProtocolV uint16
}

func (hp *HelloPacket) Build() {
	hp.BasePacket = NewBasePacket(1)
}
