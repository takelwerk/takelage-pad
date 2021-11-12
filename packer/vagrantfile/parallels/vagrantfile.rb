# frozen_string_literal: true

Vagrant.configure(2) do |config|
  config.vm.hostname = 'takelpad'
  config.vm.network :public_network
  config.vm.provider 'parallels' do |vb|
    vb.name = 'takelpad'
    vb.memory = 1024
    vb.cpus = 1
    vb.gui = false
  end
  config.vm.provision 'shell', run: 'always', inline: <<-SHELL
    /usr/local/bin/takelpad --summary
  SHELL
end
