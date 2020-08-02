# frozen_string_literal: true

Vagrant.configure(2) do |config|
  config.vm.network :public_network
  config.vm.provision 'shell', run: 'always', inline: <<-SHELL
    /usr/local/bin/takelpad
  SHELL
end
