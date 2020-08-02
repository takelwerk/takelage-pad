# frozen_string_literal: true

Vagrant.configure(2) do |config|
  config.vm.hostname = 'takelpad'
  config.vm.network :public_network
  config.vm.provider :virtualbox do |vb|
    vb.name = 'takelpad'
  end
  config.vm.provision 'shell', run: 'always', inline: <<-SHELL
    /usr/local/bin/takelpad --summary
  SHELL
end
