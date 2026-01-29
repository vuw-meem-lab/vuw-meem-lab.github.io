-- people-links.lua: Quarto filter for custom link commands
local function make_link_command(cmd, url_prefix)
  return function(args, kwargs)
    local name = pandoc.utils.stringify(args[1])
    local url = url_prefix .. (kwargs[1] or name:gsub(" ", ""))
    return pandoc.Link(name, url)
  end
end

return {
  {RawInline = function(el)
    if el.text:match('^\\linkedin') then
      local name = el.text:match('{(.-)}') or ""
      local url = "https://www.linkedin.com/in/" .. name:gsub(" ", "")
      return pandoc.Link(name, url)
    elseif el.text:match('^\\projectlink') then
      local name = el.text:match('{(.-)}') or ""
      local url = "https://www.example.com/projects/" .. name:gsub(" ", "")
      return pandoc.Link(name, url)
    elseif el.text:match('^\\fundinglink') then
      local name = el.text:match('{(.-)}') or ""
      local url = "https://www.example.com/funders/" .. name:gsub(" ", "")
      return pandoc.Link(name, url)
    end
  end}
}
