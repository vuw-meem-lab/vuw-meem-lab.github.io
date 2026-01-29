-- people-profile.lua: Quarto Lua filter for rendering people profiles from markdown files
local lfs = require("lfs")
local yaml = require("lyaml")

local function read_file(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local content = f:read("*a")
  f:close()
  return content
end

local function parse_yaml_and_bio(content)
  local yaml_start, yaml_end = content:find("%-%-%-%s*\n(.-)%-%-%-%s*\n", 1)
  if not yaml_start then return nil, nil end
  local yaml_block = content:match("%-%-%-%s*\n(.-)%-%-%-%s*\n")
  local bio = content:sub(yaml_end + 1):gsub("^\n+", "")
  local ok, meta = pcall(yaml.load, yaml_block)
  if not ok then return nil, nil end
  return meta, bio
end

local function render_profile(meta, bio)
  local photo = meta.photo or "images/placeholder.png"
  local name = meta.name or "[No Name]"
  local pronouns = meta.pronouns and (" (" .. meta.pronouns .. ")") or ""
  local role = meta.role and ("<div class='person-role'>" .. meta.role .. "</div>") or ""
  local project = meta.project and ("<div class='person-project'>" .. meta.project .. "</div>") or ""
  local links = ""
  if meta.links then
    for k, v in pairs(meta.links) do
      local icon = k == "linkedin" and "<i class='bi bi-linkedin'></i>" or k == "project" and "<i class='bi bi-link-45deg'></i>" or k == "funding" and "<i class='bi bi-cash'></i>" or ""
      links = links .. string.format("<a href='%s' target='_blank' class='person-link person-link-%s'>%s</a> ", v, k, icon)
    end
    if links ~= "" then links = "<div class='person-links'>" .. links .. "</div>" end
  end
  return string.format([[<div class='person-card'>
    <img src='%s' class='person-photo' alt='%s'>
    <div class='person-info'>
      <span class='person-name'>%s</span>%s
      %s
      %s
      %s
      <div class='person-bio'>%s</div>
    </div>
  </div>]], photo, name, name, pronouns, role, project, links, bio or "")
end

function Pandoc(doc)
  for i,el in ipairs(doc.blocks) do
    if el.t == "RawBlock" and el.format:match("^html$") and el.text:match("{{<%s*people%-list%s*>}}") then
      local people_dir = "people"
      local profiles = {}
      for file in lfs.dir(people_dir) do
        if file:match("%.md$") or file:match("%.qmd$") then
          local content = read_file(people_dir .. "/" .. file)
          if content then
            local meta, bio = parse_yaml_and_bio(content)
            if meta then
              table.insert(profiles, render_profile(meta, bio))
            end
          end
        end
      end
      local html = '<div class="people-list">' .. table.concat(profiles, "\n") .. '</div>'
      doc.blocks[i] = pandoc.RawBlock("html", html)
    end
  end
  return doc
end
