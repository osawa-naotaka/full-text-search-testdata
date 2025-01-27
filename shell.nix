let pkgs = import <nixpkgs> { };

in pkgs.mkShell rec {
  name = "python-dev";

  buildInputs = with pkgs; [
    git
    python312
    python312Packages.requests
    python312Packages.langdetect
    python312Packages.mecab-python3
    python312Packages.unidic-lite
    python312Packages.mwparserfromhell
    python312Packages.tqdm
    python312Packages.fugashi
    python312Packages.unidic-lite
    python312Packages.beautifulsoup4
    nodejs_23
    php84
    php84Packages.composer
    pandoc
  ];
}
