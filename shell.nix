let pkgs = import <nixpkgs> {};

in pkgs.mkShell rec {
  name = "python-dev";

  buildInputs = with pkgs; [
    python312
    python312Packages.requests
    python312Packages.langdetect
    python312Packages.mecab-python3
    python312Packages.unidic-lite
    python312Packages.mwparserfromhell
    python312Packages.tqdm
  ];
}
