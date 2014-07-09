package fkt

import "../fkp"

type Terminal struct {
	Server *fkp.FKServer
	Client *fkp.FKClient
}

func NewTerminal() Terminal {
	s := fkp.NewFKServer("1")
	c := fkp.NewFKClient("1")
	return Terminal{
		Server: &s,
		Client: &c,
	}
}

func (t *Terminal) RunCLI() {

}
