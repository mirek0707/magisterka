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
            pkgs.python311Full:3.11.7
            pkgs.python311Packages.scrapy:2.11.0
            pkgs.python311Packages.scrapy-splash:0.9.0
          ];

          shellHook = ''
            echo "happy web scraping ☺☺☺"
          '';
        };
  };
}
