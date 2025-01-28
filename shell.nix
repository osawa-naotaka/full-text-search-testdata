let pkgs = import <nixpkgs> { };

in pkgs.mkShell rec {
  name = "python-dev";

  buildInputs = with pkgs; [
    git
    pyenv
    python312
    python312Packages.requests
    python312Packages.mecab-python3
    python312Packages.unidic-lite
    python312Packages.mwparserfromhell
    python312Packages.beautifulsoup4
    nodejs_23
  ];
}
