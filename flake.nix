{
  description = "web scarping flake";
  nixConfig = {
    bash-prompt = ''\[\033[01;32m\]nix-develop $\[\033[00m\]\[\033[01;36m\] \w >\[\033[00m\] '';
  };

  inputs = {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    scrapy =
      pkgs.mkShell
        {
          buildInputs = [
            pkgs.python311Full
            pkgs.python311Packages.scrapy
            pkgs.python311Packages.scrapy-splash
      	    pkgs.python311Packages.pymongo
      	    pkgs.python311Packages.python-dateutil
            pkgs.python311Packages.fastapi
            pkgs.python311Packages.uvicorn
            pkgs.python311Packages.motor
            pkgs.mongosh
            pkgs.python311Packages.pydantic-extra-types
            pkgs.python311Packages.email-validator
          ];

          shellHook = ''
            echo "happy web scraping ☺☺☺"
          '';
        };
  };
}
