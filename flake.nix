{
  description = "python+poetry";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        commonLibs = [
          pkgs.pkg-config
          pkgs.openssl
          pkgs.zlib
          pkgs.sqlite
          pkgs.libffi
          pkgs.readline
        ];

        mkPythonShell = python: pkgs.mkShell {
          buildInputs = [ pkgs.poetry python ] ++ commonLibs;
          shellHook = ''
            echo "poetry + ${python.pname} ${python.version} ready"
          '';
        };

      in {
        devShells = {
          default = mkPythonShell pkgs.python312;
        };
      });
}
